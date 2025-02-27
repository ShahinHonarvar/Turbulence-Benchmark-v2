def palindromes_between_indices(s):
    letters = [char for char in s[2:6] if char.isalpha()]
    letters = [char.lower() for char in letters]
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for perm in permutations(letters, i):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes