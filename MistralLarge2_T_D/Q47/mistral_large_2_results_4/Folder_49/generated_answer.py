def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    substring = s[10:101].lower()
    length = len(substring)
    palindromes = set()
    for i in range(length):
        for j in range(i + 10, min(i + 51, length + 1)):
            segment = substring[i:j]
            if segment.isalpha() and is_palindrome(segment):
                palindromes.add(segment)
    return palindromes