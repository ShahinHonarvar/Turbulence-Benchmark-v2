import sys
import heapq
from collections import defaultdict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce
from operator import add, sub
from heapq import heappush, heappop
from itertools import permutations, accumulate
from math import sqrt, log2, factorial
from collections import Counter

def main():
    x = int(input())
    return list(filter(lambda p: check_digit(p), list(range(2, x + 1))))