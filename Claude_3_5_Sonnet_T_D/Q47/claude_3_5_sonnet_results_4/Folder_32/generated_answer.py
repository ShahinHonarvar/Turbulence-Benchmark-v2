def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[16:78]
    for i in range(len(substring)):
        for j in range(i + 43, min(i + 48, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha():
                lowercase_palindrome = potential_palindrome.lower()
                if lowercase_palindrome == lowercase_palindrome[::-1]:
                    result.add(potential_palindrome)
    return result