from string import ascii_lowercase

def palindromes_between_indices(input_string):
    output = set()
    available_letters = {char for char in input_string.lower() if char in ascii_lowercase and input_string.lower().index(char) >= 5 and (input_string.lower().index(char) <= 9)}
    for indices in range(len(available_letters) - 4):
        for combination in itertools.combinations(available_letters, indices + 5):
            if combination not in output:
                output.add(''.join(sorted(combination)))
    return output