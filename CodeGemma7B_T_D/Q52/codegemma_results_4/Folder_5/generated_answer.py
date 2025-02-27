import re

def palindrome_of_length_n(s):
    answer = set()
    for i in range(len(s)):
        for j in range(i + 16, len(s)):
            word = re.sub('[^A-Za-z]', '', s[i:j + 1])
            if word == word[::-1]:
                answer.add(word)
    return answer