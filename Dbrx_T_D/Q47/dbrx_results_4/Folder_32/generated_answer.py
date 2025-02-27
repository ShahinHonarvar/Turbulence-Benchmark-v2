def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for length in range(43, 48):
        for i in range(16, len(s) - length + 1):
            palindrome = s[i:i + length]
            if palindrome.lower() == palindrome and set(palindrome) <= english_letters:
                result.add(palindrome)
    return result