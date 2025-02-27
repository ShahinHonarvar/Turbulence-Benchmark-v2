def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    start_index, end_index = (3, 4)
    if end_index >= len(s) or s[start_index:end_index + 1].isalpha() == False:
        return palindromes
    for i in range(start_index, end_index + 1):
        for j in range(i, end_index + 1):
            substring = s[i:j + 1].lower()
            if substring[0] != substring[-1] or substring[0] in english_letters:
                continue
            palindrome = substring[0] + ''.join(reversed(substring[1:-1])) + substring[-1]
            palindromes.add(palindrome)
    return palindromes