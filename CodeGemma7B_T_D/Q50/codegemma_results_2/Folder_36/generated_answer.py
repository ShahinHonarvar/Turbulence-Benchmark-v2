from itertools import combinations

def if_contains_anagrams(text_list):
    anagrams = []
    for text in text_list:
        sorted_text = ''.join(sorted(text.lower()))
        if len(sorted_text) >= 3:
            anagrams.append(sorted_text)
    pairs_count = 0
    for txt1, txt2 in combinations(anagrams, 2):
        if txt1 == txt2:
            pairs_count += 1
        if pairs_count >= 312:
            return True
    return False