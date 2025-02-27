def palindrome_of_length_at_least_n(text):
    return set((pal for pal in substrings(text) if is_palindrome(pal) and len(pal) >= 55))

def substrings(text):
    return {text[i:j] for i in range(len(text)) for j in range(i + 1, len(text) + 1)}

def is_palindrome(text):
    return text.lower() == text.lower()[::-1]