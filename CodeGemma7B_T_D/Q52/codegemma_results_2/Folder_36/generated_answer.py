def palindrome_of_length_n(text):
    ans = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if is_palindrome(text[i:j + 1]):
                ans.add(text[i:j + 1])
    return ans

def is_palindrome(text):
    return text == text[::-1]