from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindrome_count = defaultdict(int)
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                palindrome_count[text[i:j + 1]] += 1
    return {palindrome for palindrome, count in palindrome_count.items() if count >= 147}