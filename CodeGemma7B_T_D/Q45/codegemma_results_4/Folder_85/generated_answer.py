from itertools import permutations

def palindromes_between_indices(input_string):
    input_string = input_string.lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    result = set()
    for i in range(len(input_string) - 6):
        substring = input_string[i:i + 7]
        if substring[0] in english_letters and substring[6] in english_letters:
            permutations_substring = permutations(substring)
            for p in permutations_substring:
                palindrome = ''.join(p)
                if palindrome.startswith(substring[0]) and palindrome.endswith(substring[6]):
                    result.add(palindrome)
    return result