from collections import Counter

def if_contains_anagrams(word_list):
    counter_word = Counter()
    for word in word_list:
        if len(word) < 3:
            continue
        counter_word[word.lower()] += 1
    count = 0
    length = len(word_list)
    for word, frequency in counter_word.items():
        if frequency > 1 and length - frequency > 1:
            count += frequency * (frequency - 1) // 2
    return count >= 246