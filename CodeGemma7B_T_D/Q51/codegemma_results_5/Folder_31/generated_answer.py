def if_contains_anagrams(strings):
    two_gram_count = {}
    three_gram_count = {}
    for string in strings:
        string = string.lower()
        for i in range(len(string) - 2):
            two_gram = string[i:i + 2]
            three_gram = string[i:i + 3]
            if len(two_gram) == 2 and two_gram not in two_gram_count:
                two_gram_count[two_gram] = 0
            two_gram_count[two_gram] += 1
            if len(three_gram) == 3 and three_gram not in three_gram_count:
                three_gram_count[three_gram] = 0
            three_gram_count[three_gram] += 1
    anagram_pairs = sum((count ** 2 for count in two_gram_count.values())) / 2 + sum((count ** 2 for count in three_gram_count.values())) / 2
    return anagram_pairs <= 65