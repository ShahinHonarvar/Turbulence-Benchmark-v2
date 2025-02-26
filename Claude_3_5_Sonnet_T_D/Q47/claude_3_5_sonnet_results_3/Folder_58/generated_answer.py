def palindromes_of_specific_lengths(s):
    substring = s[125:284]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 109, min(i + 127, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 109 and len(potential_palindrome) <= 126:
                if potential_palindrome == potential_palindrome[::-1]:
                    result.add(potential_palindrome)
    return result