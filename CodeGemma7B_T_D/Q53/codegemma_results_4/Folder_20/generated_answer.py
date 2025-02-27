from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    word_count = defaultdict(int)
    for word in text.split():
        word_count[word] += 1
    result = set()
    for word, count in word_count.items():
        length = len(word)
        if length >= 66 and word == word[::-1]:
            for i in range(2, count + 1):
                result.add(word * i)
    return result