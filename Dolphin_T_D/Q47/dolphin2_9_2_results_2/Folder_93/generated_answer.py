def palindromes_of_specific_lengths(s):
    substring = s[17:96]
    palindromes = set()
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            possible_palindrome = substring[i:i + length]
            if possible_palindrome == possible_palindrome.lower() and possible_palindrome == possible_palindrome[::-1] and (len(set(possible_palindrome.lower()) & set('abcdefghijklmnopqrstuvwxyz')) == len(possible_palindrome.lower())):
                palindromes.add(possible_palindrome)
    return palindromes