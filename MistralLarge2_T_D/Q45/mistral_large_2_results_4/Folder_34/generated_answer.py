import itertools

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[5:8])).lower()
    letters = set(substring)
    result = set()
    for length in range(4, len(substring) + 1):
        for combo in itertools.combinations_with_replacement(letters, length // 2):
            palindrome = ''.join(combo + combo[-(length // 2):][::-1])
            result.add(palindrome)
    return result