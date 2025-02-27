from collections import defaultdict

def palindrome_of_length_n(text):
    text = text.lower()
    palindrome = defaultdict(list)
    for i in range(len(text)):
        for j in range(i + 131, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindrome[j - i].append(substring)
    return {len(palindrome[k]): palindrome[k] for k in palindrome}