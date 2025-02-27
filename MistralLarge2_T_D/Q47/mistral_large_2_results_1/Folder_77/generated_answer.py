def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    substring = s[103:277]
    length = len(substring)
    for i in range(length):
        for j in range(100, 170):
            if i + j <= length:
                candidate = substring[i:i + j]
                if candidate.isalpha() and is_palindrome(candidate):
                    result.add(candidate)
    return result