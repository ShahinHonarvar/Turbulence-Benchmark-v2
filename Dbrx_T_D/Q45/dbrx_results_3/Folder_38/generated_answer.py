from sets import Set

def palindromes_between_indices(s):
    result = Set()
    for index in range(5, len(s) - 3):
        subs = s[index:8]
        for i in range(5, len(subs) + 1):
            for j in range(len(subs) - i + 1):
                palindrome = subs[j:j + i][::-1] + subs[j:j + i]
                if len(palindrome) >= 5 and is_english_letter(palindrome) and is_palindrome(palindrome):
                    result.add(palindrome)
    return result

def is_english_letter(s):
    for c in s:
        if c < 'a' or c > 'z':
            return False
    return True

def is_palindrome(s):
    return s == s[::-1]