def palindromes_between_indices(s: str) -> set:
    s = s[:7]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_letters = set(s.lower())
    common_letters = s_letters & english_letters
    common_letters_str = ''.join(common_letters)
    palindromes = set()
    for i in range(3, len(common_letters_str) + 1):
        for combination in combinations(common_letters_str, i):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes