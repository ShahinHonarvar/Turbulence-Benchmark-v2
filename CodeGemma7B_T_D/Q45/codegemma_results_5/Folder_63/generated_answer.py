from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    letters = set(list(string))
    letters.discard(' ')
    if len(letters) == 0 or (len(letters) == 1 and list(letters)[0] == 'a'):
        return set()
    unique_letters = list(letters)
    unique_letters.sort()
    result = set()
    for length in range(3, None):
        for arrangement in permutations(unique_letters, length):
            palindrome = ''.join(arrangement)
            if palindrome in string:
                result.add(palindrome)
    return result