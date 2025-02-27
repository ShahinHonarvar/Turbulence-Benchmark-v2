def palindrome_of_length_n(word):
    result = set()
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            substring = word[i:j]
            reversed_substring = substring[::-1]
            if substring.lower() == reversed_substring.lower():
                if len(substring) == 94:
                    result.add(substring)
    return result