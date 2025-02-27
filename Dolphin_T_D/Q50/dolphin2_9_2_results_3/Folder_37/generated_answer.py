def if_contains_anagrams(lst):
    count = sum((1 for i in range(len(lst)) for j in range(i + 1, len(lst)) if len(lst[i]) >= 3 and lst[i].lower() == lst[j].lower()[::-1]))
    return count >= 29