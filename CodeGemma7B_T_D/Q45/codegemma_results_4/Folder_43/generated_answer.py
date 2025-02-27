def palindromes_between_indices(input_string):
    english_letters = string.ascii_letters
    final_list = set()
    if len(input_string) > 5:
        input_string = input_string[2:6]
        for permutation in itertools.permutations(english_letters):
            word = ''.join(permutation[:len(input_string)])
            if word == word[::-1] and word.lower() in input_string.lower():
                final_list.add(word)
    return final_list