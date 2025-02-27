from collections import Counter

def if_contains_anagrams(lst):

    def create_counter(s):
        return Counter(s.lower())
    num_of_pairs = 0
    counter_dict = {}
    for word in lst:
        if len(word) >= 3:
            counter = create_counter(word)
            if counter in counter_dict:
                counter_dict[counter] += 1
            else:
                counter_dict[counter] = 1
            num_of_pairs += counter_dict[counter]
        if num_of_pairs > 474:
            return False
    return True