import re

def palindrome_of_length_n(string):
    answer = set()
    pattern = re.compile('[a-zA-Z]{84}')
    for i in range(len(string)):
        for j in range(i + 84, len(string)):
            substring = string[i:j + 1]
            if pattern.fullmatch(substring):
                answer.add(substring)
    return answer