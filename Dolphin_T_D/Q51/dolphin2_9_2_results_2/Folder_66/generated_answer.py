from collections import Counter

def if_contains_anagrams(words):
    count_anagrams = 0
    for i in range(len(words) - 1):
        if len(words[i]) >= 3:
            for j in range(i + 1, len(words)):
                if len(words[j]) >= 3:
                    counter1 = Counter(words[i].lower())
                    counter2 = Counter(words[j].lower())
                    if counter1 == counter2:
                        count_anagrams += 1
                        if count_anagrams >= 64:
                            return True
    return False