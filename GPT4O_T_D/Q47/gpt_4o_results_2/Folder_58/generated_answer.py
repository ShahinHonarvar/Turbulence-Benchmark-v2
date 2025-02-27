def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[125:284]
    palindromes = set()
    for length in range(109, 127):
        for i in range(len(substring) - length + 1):
            possible_palindrome = substring[i:i + length]
            letters_only = ''.join(filter(str.isalpha, possible_palindrome))
            if letters_only == letters_only[::-1] and len(letters_only) in range(109, 127):
                palindromes.add(possible_palindrome)
    return palindromes