def palindromes_of_specific_lengths(s):
    s = s[101:293].lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    filtered_s = ''.join(filter(valid_chars.__contains__, s))
    min_len, max_len = (154, 182)
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    length = len(filtered_s)
    for start in range(length):
        for end in range(start + min_len, min(start + max_len + 1, length + 1)):
            substring = filtered_s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes