def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    letters_in_range = {char for char in s[:6] if char in english_letters}
    for p_length in range(6, len(letters_in_range) * 2 + 1):
        for p in permutations(letters_in_range, p_length):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes