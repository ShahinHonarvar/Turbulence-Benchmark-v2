def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 17):
        for j in range(i + 18, len(text) + 1):
            substring = text[i:j]
            if ''.join([i for i in substring.lower() if i.isalpha()]) == ''.join(reversed([i for i in substring.lower() if i.isalpha()])):
                palindromes.add(substring)
    return palindromes