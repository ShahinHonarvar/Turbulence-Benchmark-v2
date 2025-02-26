def palindromes_of_specific_lengths(s):
    substring = s[63:71]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 4, i + 6):
            if j <= len(substring):
                potential_palindrome = substring[i:j]
                if potential_palindrome.isalpha():
                    if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                        result.add(potential_palindrome)
    return result