from collections import defaultdict

def palindrome_of_length_n(s):
    word_dict = defaultdict(list)
    for i in range(len(s)):
        for j in range(i + 1, min(i + 200, len(s))):
            word_dict[s[i:j + 1].lower()].append(s[i:j + 1])
    output = set()
    for key in word_dict:
        if len(key) == 210:
            output.add(key)
    return output