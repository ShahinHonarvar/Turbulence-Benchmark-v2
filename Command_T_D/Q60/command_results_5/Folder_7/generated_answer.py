import bisect
import functools
from collections import namedtuple

def generate_left_right_truncatable_primes(n):
    primes = generate_primes(n)
    left_right_truncatable_primes = []
    left_right_truncatable_pairs = []
    left_right_truncatable_triplets = []
    left_right_truncatable_quadruplets = []
    left_right_truncatable_quintuplets = []
    left_right_truncatable_sextuplets = []
    left_right_truncatable_septuplets = []
    left_right_truncatable_octuplets = []
    left_right_truncatable_nonuplets = []
    left_right_truncatable_pairs = []
    left_right_truncatable_triplets = []