def palindromes_between_indices(string):
    letters = set([char.lower() for char in string[4:8]])
    return set() if len(letters) < 2 else set([''.join(palindrome) for i in range(4, len(string)) for j in range(i + 3, len(string) + 1) for palindrome in permutations(string[i:j]) if palindrome == palindrome[::-1] and all([char in letters for char in palindrome])])