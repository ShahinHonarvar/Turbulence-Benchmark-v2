def palindromes_of_specific_lengths(s):
    substring = s[10:60]
    requirement = ''
    palindromes = set()
    for length in range(18, 37):
        for i in range(len(substring)):
            requirement = ''
            for j in range(i, i + length):
                requirement += substring[j].lower()
                if is_palindrome(requirement) and requirement.isalpha():
                    palindromes.add(requirement)
    return palindromes

def is_palindrome(s):
    return s == s[::-1]