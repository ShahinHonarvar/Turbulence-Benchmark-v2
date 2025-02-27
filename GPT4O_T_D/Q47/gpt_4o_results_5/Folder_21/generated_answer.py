from re import findall

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    subs = set()
    substring = s[100:296]
    substring_clean = ''.join(findall('[a-zA-Z]', substring))
    n = len(substring_clean)
    for length in range(136, 161):
        for i in range(n - length + 1):
            sub = substring_clean[i:i + length].lower()
            if is_palindrome(sub):
                subs.add(sub)
    return subs