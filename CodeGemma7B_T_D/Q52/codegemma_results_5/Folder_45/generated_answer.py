def palindrome_of_length_n(text):
    ans = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text), 21):
            if text[i:j + 21].lower().replace(' ', '') == text[i:j + 21].lower().replace(' ', '')[::-1]:
                ans.add(text[i:j + 21])
    return ans