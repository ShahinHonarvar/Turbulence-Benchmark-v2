import string

def palindromes_between_indices(s):
    letters = string.ascii_lowercase
    palindromes = set()
    substring = s[4:10].lower()
    for a1 in letters:
        if a1 in substring:
            for a2 in string.ascii_letters:
                if substring.count(a1) > 0:
                    for a3 in string.ascii_letters:
                        if substring.count(a1) > 0 and substring.count(a2) > 0 and (substring.count(a3) > 0):
                            palindrome = a1 + a2 + a1
                            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                                palindromes.add(palindrome)
    return palindromes