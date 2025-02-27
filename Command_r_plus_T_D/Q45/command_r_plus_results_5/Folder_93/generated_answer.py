def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_range = s[2:8]
    filtered_s_range = ''.join((char for char in s_range if char in english_letters))
    palindromes = set()
    for i in range(len(filtered_s_range)):
        for j in range(i + 6, len(filtered_s_range) + 1):
            substring = filtered_s_range[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes