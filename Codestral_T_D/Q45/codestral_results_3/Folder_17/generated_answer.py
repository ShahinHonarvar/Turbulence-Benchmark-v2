def palindromes_between_indices(string):

    def is_palindrome(s):
        return s == s[::-1]
    substring = string[2:7].lower()
    unique_chars = set(substring)
    palindromes = set()
    for char in unique_chars:
        count = substring.count(char)
        if count >= 2:
            remaining_chars = substring.replace(char, '', 2)
            for i in range(len(remaining_chars) + 1):
                for j in range(i, len(remaining_chars) + 1):
                    palindrome = remaining_chars[:i] + char + remaining_chars[i:j] + char + remaining_chars[j:]
                    if len(palindrome) >= 4 and is_palindrome(palindrome):
                        palindromes.add(palindrome)
    return palindromes