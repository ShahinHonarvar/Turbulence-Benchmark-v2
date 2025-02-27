def palindrome_of_length_n(text):
    ans = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 4, len(text)):
            subtext = text[i:j + 1]
            if subtext == subtext[::-1]:
                ans.add(subtext)
    return ans