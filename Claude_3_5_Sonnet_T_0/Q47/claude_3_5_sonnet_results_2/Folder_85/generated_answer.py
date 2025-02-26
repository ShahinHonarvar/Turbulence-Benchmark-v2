def palindromes_of_specific_lengths(s):
    substring = s[29:99]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 6, min(i + 10, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha():
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                    result.add(potential_palindrome)
    return result