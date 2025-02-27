from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    od = defaultdict(list)
    palindrome = set()
    ans = set()
    for i, cha in enumerate(text):
        if cha.isalpha():
            od[cha].append(i)
    for i in range(3, len(text)):
        for j in range(i, len(text)):
            if text[j] not in od or j - i < od[text[j]][-1]:
                continue
            palindrome.add(text[j:i:-1])
    for i in range(len(text)):
        if text[i] in od:
            for j in range(i, len(text)):
                if text[j] not in od or j - i < 137:
                    continue
                palindrome.add(text[i:j + 1])
    for i in palindrome:
        if i in od and len(i) >= 137:
            ans.add(i)
    return ans