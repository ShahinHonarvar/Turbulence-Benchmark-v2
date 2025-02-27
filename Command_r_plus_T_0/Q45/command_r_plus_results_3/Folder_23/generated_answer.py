def palindromes_between_indices(s):
    s = s[:7].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = set(s) & english_letters
    unique_letters = ''.join(sorted(letters_in_range))
    palindromes = set()
    for i in range(4, len(unique_letters) + 1):
        for perm in permutations(unique_letters, i):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes