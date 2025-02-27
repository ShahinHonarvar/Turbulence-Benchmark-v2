def palindrome_of_length_n(word):
    longest_palindrome = ''
    palindrome_set = set()
    for i in range(len(word)):
        for j in range(i, len(word)):
            substring = word[i:j + 1]
            if substring == substring[::-1]:
                lowercased_substring = substring.lower()
                if len(lowercased_substring) == 113 and lowercased_substring not in palindrome_set:
                    palindrome_set.add(lowercased_substring)
    return palindrome_set