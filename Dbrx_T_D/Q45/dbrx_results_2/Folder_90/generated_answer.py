from functools import reduce

def find_all_permutations(chars):
    if len(chars) == 1:
        return [chars]
    return reduce(lambda result, perm: result + [char + perm for char in chars for perm in result if char not in perm], find_all_permutations(chars[:-1]), [chars[0]])

def is_palindrome(string):
    return string == string[::-1]

def palindromes_between_indices(string):
    if len(string) == 0:
        return set()
    chars = [char.lower() for char in string[:6] if char.isalpha()]
    permutations = find_all_permutations(chars)
    palindromes = [perm for perm in permutations if is_palindrome(perm)]
    palindromes = [palindrome for palindrome in palindromes if len(palindrome) >= 4]
    return set(palindromes)