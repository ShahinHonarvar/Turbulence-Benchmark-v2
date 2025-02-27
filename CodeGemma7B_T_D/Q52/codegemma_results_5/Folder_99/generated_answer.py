def palindrome_of_length_n(text):
    text = text.lower()
    ans = set()
    length = len(text)
    for i in range(length):
        for j in range(i, length):
            if j - i + 1 == 420:
                ans.add(text[i:j + 1])
    return ans