from itertools import combinations
    from string import ascii_letters

def palindromes_between_indices(s):
    substring = s[2:10]
    index_to_letter = {v: k for k, v in enumerate(ascii_letters)}
    palindromes = set()
    for length in range(6, len(substring) + 1):
        for perm in combinations(substring, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                for letter in palindrome:
                    if letter not in index_to_letter:
                        break
                else:
                    palindromes.add(palindrome.lower())
    return palindromes