def palindromes_between_indices(s):
    letters = [char for char in s[2:6] if char.isalpha()]
    letters = [char.lower() for char in letters]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            if str(perm) == str(perm)[::-1]:
                palindromes.add(str(perm))
    return palindromes