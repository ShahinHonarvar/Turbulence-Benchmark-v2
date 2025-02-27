def palindromes_between_indices(s):
    s = s[:5].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_letters = set(s)
    common_letters = s_letters & english_letters
    common_letters_str = ''.join(common_letters)
    palindromes = set()
    for i in range(len(common_letters_str)):
        for j in range(i + 3, len(common_letters_str) + 1):
            substr = common_letters_str[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes