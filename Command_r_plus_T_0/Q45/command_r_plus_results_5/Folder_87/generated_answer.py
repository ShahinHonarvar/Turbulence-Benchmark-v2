def palindromes_between_indices(s):
    substring = s[3:10].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_substring = ''.join((char for char in substring if char in english_letters))
    palindromes = set()
    for i in range(len(filtered_substring)):
        for j in range(i + 3, len(filtered_substring) + 1):
            palindrome = filtered_substring[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes